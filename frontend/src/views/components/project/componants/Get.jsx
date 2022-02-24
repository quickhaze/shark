import React, { useState } from "react";

const Get = () => {
    let listdata = ''

    const[data1, setData] = useState(listdata)
    listdata = data1
    fetch("http://127.0.0.1:8006/info/info_create/1")
    .then(
        response => {
            return response.json();
        }
    )
    .then(
        data => {
            // console.log(data)
            let pr = {name : "Neeraj"}
            setData(pr) 
            console.log(data1)
            
        }
        )
        
        return(
            <><h2>{listdata}</h2></>
    )
}

export default Get;