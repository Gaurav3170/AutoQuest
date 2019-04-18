var mongoose = require("mongoose");
 
var questionSchema = new mongoose.Schema({
    subject: String,
    unit: String,
    level: String,
    question: String,
    author: {
        id: {
            type: mongoose.Schema.Types.ObjectId,
            ref: "User"
        },
        username: String
    }
});
 
module.exports = mongoose.model("question", questionSchema);