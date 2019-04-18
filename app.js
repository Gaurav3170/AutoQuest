var express = require("express");
var app = express();
var bodyParser = require("body-parser");
var mongoose = require("mongoose");

var passport = require("passport");
var LocalStrategy = require("passport-local");
var User       = require("./models/user");
var Question   =require("./models/question");



mongoose.connect("mongodb://localhost:27017/AutoQuest_v3", {useNewUrlParser: true});
app.use(bodyParser.urlencoded({extended:true}));
app.set("view engine", "ejs");

app.use(express.static(__dirname + "/public"));
//===================================================
//PASSPORT CONFIG
//===================================================
app.use(require("express-session")({
    secret: "This is the text for hashing",
    resave: false,
    saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());





app.use(function(req, res, next){
    res.locals.currentUser = req.user;
    next();
});



//---------------------------------------
// ROUTES
//----------------------------------------

app.get("/", function(req, res){
    res.render("landing");
});

app.get("/intro", function(req, res){
    res.render("intro");
});

app.get("/dashboard", isLoggedIn, function(req, res){
   res.render("dashboard"); 
});




app.get("/questions", function(req, res){
       Question.find({}, function(err, allQuestion){
         if(err){
             console.log(err);
         } else {
             res.render("questions", {questions: allQuestion});
         }
        
     }); 
});

app.get("/questions/new", isLoggedIn, function(req, res){
    res.render("new");
});


app.post("/questions", function(req, res){
    var subject = req.body.subject;
    var unit    = req.body.unit;
    var level   =req.body.level;
    var question = req.body.question;
    var newQuestion = {subject: subject, unit: unit, level: level,question: question};
    console.log(newQuestion);
     Question.create(newQuestion, function(err, newlyCreated){
        if(err){
            console.log(err);
        } else {
            res.redirect("/questions/new");
        }
    });
    
});



//========================================
//Auth Routes
//======================================


//shows login/signup form

app.get("/register", function(req, res) {
    res.render("login");
});

//handles Sign up logic

app.post("/register", function(req, res){
     var newUser = new User({username: req.body.username, name:req.body.name});
     User.register(newUser, req.body.password, function(err, user){
       if(err){
           console.log(err);
           return res.render("login");
       } else {
           passport.authenticate("local")(req, res, function(){
               res.redirect("dashboard");
           });
       }
   });
});



// show login form

app.get("/login", function(req, res){
   res.render("login"); 
});

// handling login logic

app.post("/login", passport.authenticate("local", 
    {
        successRedirect: "/dashboard",
        failureRedirect: "/login"
    }), function(req,res){

    });



//logout route
app.get("/logout", function(req, res){
    req.logout();
    res.redirect("/");
});


function isLoggedIn(req, res, next){
    if(req.isAuthenticated()){
        return next();
    } res.redirect("/login");
}






app.listen(process.env.PORT, process.env.IP, function(){
    console.log("AutoQuest Server has started...");
});