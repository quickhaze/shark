
import React from "react";
import App from "../../../App";
import Get from "../project/componants/Get";
import './Layout.css'

let Layout = () => {



    return (
        <>
            <div className="row" id="wrapper">
                <div className="col-2 border-end bg-dark side-bar" id="sidebar-wrapper">
                    <div className="sidebar-heading border-bottom bg-dark"><h1>Start Bootstrap</h1><br /></div>
                    
                    <div className="list-group list-group-flush">
                        <a className="list-group-item list-group-item-action list-group-item-light p-3 bg-dark b" href="#!"><b>Dashboard</b></a>
                        <a className="list-group-item list-group-item-action list-group-item-light p-3 bg-dark b" href="#!"><b>Projects</b></a>
                        <a className="list-group-item list-group-item-action list-group-item-light p-3 bg-dark b" href="http://localhost:3000/userinfo/"><b>Members</b></a>
                        <a className="list-group-item list-group-item-action list-group-item-light p-3 bg-dark b" href="#!"><b>Trainee</b></a>
                        <a className="list-group-item list-group-item-action list-group-item-light p-3 bg-dark b" href="#!"><b>Login</b> </a>
                    </div>
                </div>
                <div className="col-10" id="page-content-wrapper">

                    <div className="container-fluid">
                        <App />

                        {/* <Get /> */}
                    </div>
                </div>
            </div>




        </>
    )

}



export default Layout;