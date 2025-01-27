import express from 'express'

// initialised/created project
const app = express()
const PORT = process.env.PORT || 3000

// return information
app.get('/employees', (req,res)=>{
    res.json({
        message:"This is the GET employees path"
    })
})
app.get('/managers', (req,res)=>{
    res.json({
        message:"This is the GET managers path"
    })
})
app.post('/employees', (req,res)=>{
    res.json({
        message:"This is the POST employees path and you added something"
    })
})
app.post('/managers', (req,res)=>{
    res.json({
        message:"This is the POST managers path and you added something"
    })
})
app.patch('/employees', (req,res)=>{
    res.json({
        message:"This is the PUT employees path and you updated something"
    })
})
app.patch('/managers', (req,res)=>{
    res.json({
        message:"This is the PUT managers path and you updated something"
    })
})
app.delete('/employees', (req,res)=>{
    res.json({
        message:"This is the DELETE employees path and you deleted something"
    })
})
app.delete('/managers', (req,res)=>{
    res.json({
        message:"This is the DELETE managers path and you deleted something"
    })
})



// allows project to be an API
app.listen(PORT, ()=> {
    console.log('http://localhost:'+PORT);
})