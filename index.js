const express = require("express");
const { spawn } = require("child_process");

const app = express();
const port = process.env.PORT || 8000;

app.get('/getData', (req,res)=>{
    let resultData;
    console.log(`Get Data method call ----> Start`);
    const pythonProcess = spawn('python',["main1.py"]);
    pythonProcess.stdout.on('data',function(data){
        resultData = data.toString();
        resultData = JSON.parse(resultData);
        console.log(`Print the Data----> `);
        console.log(resultData);
    });

    
    setTimeout(() => {  
        
        pythonProcess.on('close', (code)=>{
            res.send(resultData)
        });

        
     }, 2000);
    console.log(`Get Data method call ----> End`);
})

app.listen(port, ()=> console.log(`node-python server running on http://localhost:${port} !`));