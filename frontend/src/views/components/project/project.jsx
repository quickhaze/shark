import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './project.css';
import { IconName } from "react-icons/fa";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faArrowRightFromFile } from '@fortawesome/free-solid-svg-icons'
import { withRouter, RouteComponentProps } from "react-router";
import { useParams } from 'react-router-dom';
import User from './User';
import './User.css'


const FeaturedProjects = (props) => {
    const params = useParams()
    // debugger
    const [projects, setProjects] = useState([]);
    useEffect(() => {
        fetchProjects();
    }, []);
    const fetchProjects = () => {
        let url = `http://127.0.0.1:8006/info/info_create/`
        if ((params.id == false) || (params.id == undefined)) {
            axios
                .get(`http://127.0.0.1:8006/info/info_create/`)
                .then((res) => {
                    setProjects(res.data)
                })
                .catch((err) => {
                    console.log(err);
                });
        }
        else {
            axios
                .get(`http://127.0.0.1:8006/info/info_create/${params.id}`)
                .then((res) => {
                    setProjects(res.data)
                })
                .catch((err) => {
                    console.log(err);
                });

        }
    };
    if ((params.id == false) || (params.id == undefined)) {
        return (
            <div>
                <h3>Employee List</h3>
                <div className="row">
                    {projects.map((project) => (
                        <div className="col-md-6 col-lg-3 g-mb-30" key={project.id}>
                            <a href={`/userinfo/` + project.id}><FontAwesomeIcon />
                                <article className="u-shadow-v18 g-bg-dark text-center rounded g-px-20 g-py-40 g-mb-5 user-box">
                                    <img className="d-inline-block img-fluid mb-4 rounded-circle img1" src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="Member image" />
                                    <h4 className="h5 g-color-black g-font-weight-600 g-mb-10">{project.user}</h4>
                                    <p className='mt'>Member/trainee</p>
                                </article>
                            </a>
                        </div>

                    ))}
                </div>
            </div>
        );
    }
    else {
        // debugger
        return (
            <>
                <h2 className='infor'>Information</h2>
                <div className="row editbtn">
                    <div className="col-10">
                    </div>
                    <div className="col-2">
                        <a className="btn edbtn text-white" target="__blank" href="">Edit info</a>
                    </div>
                </div>
                <div className="container mt-3">
                    <div className="main-body">


                        <div className="row gutters-sm">
                            <div className="col-md-4 mb-3">
                                <div className="card bg-dark">
                                    <div className="card-body left-side bg-dark">
                                        <div className="d-flex flex-column align-items-center text-center">
                                            <img className="rounded-circle img2" src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="Admin" />
                                            <div className="mt-3">
                                                <h4 className='text-white'>{projects.user}</h4>
                                                <p className="text-secondary mb-1">Full Stack Developer</p>
                                                <p className="text-muted font-size-sm">Bay Area, San Francisco, CA</p>
                                                {/* <button className="btn btn-primary">Follow</button>
                                            <button className="btn btn-outline-primary">Message</button> */}
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>
                            <div className="col-md-8 info">
                                <div className="card mb-3">
                                    <div className="card-body">
                                        <div className="row">
                                            <div className="col-sm-3">
                                                <h6 className="mb-0">Full Name</h6>
                                            </div>
                                            <div className="col-sm-9 text-secondary">
                                                {projects.user}
                                            </div>
                                        </div>
                                        <hr />
                                        <div className="row">
                                            <div className="col-sm-3">
                                                <h6 className="mb-0">Email</h6>
                                            </div>
                                            <div className="col-sm-9 text-secondary">
                                                {projects.email}
                                            </div>
                                        </div>
                                        <hr />
                                        <div className="row">
                                            <div className="col-sm-3">
                                                <h6 className="mb-0">Mobile</h6>
                                            </div>
                                            <div className="col-sm-9 text-secondary">
                                                {projects.phone_number}
                                            </div>
                                        </div>
                                        <hr />
                                        <div className="row">
                                            <div className="col-sm-3">
                                                <h6 className="mb-0">Experience</h6>
                                            </div>
                                            <div className="col-sm-9 text-secondary">
                                                {projects.experiance}
                                            </div>
                                        </div>
                                        <hr />

                                        <div className="row">
                                            <div className="col-sm-3">
                                                <h6 className="mb-0">Address</h6>
                                            </div>
                                            <div className="col-sm-9 text-secondary">
                                                Bay Area, San Francisco, CA
                                            </div>
                                        </div>

                                    </div>
                                </div>

                            </div>
                        </div>

                    </div>
                </div>
            </>
        )
    }
};
export default FeaturedProjects;


