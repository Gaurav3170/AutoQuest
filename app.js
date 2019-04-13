var express = require("express");
var app = express();
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));

//---------------------------------------
// ROUTES
//----------------------------------------

app.get("/", function(req, res){
    res.render("landing");
});

app.get("/intro", function(req, res){
    res.render("intro");
});











app.listen(process.env.PORT, process.env.IP, function(){
    console.log("AutoQuest Server has started...");
});