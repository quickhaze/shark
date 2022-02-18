import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './project.css';
import { IconName } from "react-icons/fa";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faArrowRightFromFile } from '@fortawesome/free-solid-svg-icons'
import { withRouter, RouteComponentProps } from "react-router";
import { useParams } from 'react-router-dom';

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
                <h1>Employee List</h1>
                <div className='item-container'>
                    <div className='card-list'>
                        {projects.map((project) => (
                            <div className='card'>
                                <span className='item'>
                                    User
                                </span>
                                <span className='item'>
                                    {project.user}
                                </span>
                                <span className='item'>
                                    <a href={`/userinfo/` + project.id}><FontAwesomeIcon icon={faArrowRightFromFile} /> </a>
                                </span>
                            </div>
                        ))}
                    </div>

                </div>
            </div>
        );
    }
    else {
        // debugger
        return (
            <div className='item-container'>
                <div className='card-list'>
                    <div className='card'>
                        <span className='item'>
                            User
                        </span>
                        <span className='item'>
                            {projects.user}
                        </span>
                    </div>
                    <div className='card'>
                        <span className='item'>
                        Phone Number
                        </span>
                        <span className='item'>
                            {projects.phone_number}
                        </span>
                    </div>
                    <div className='card'>
                        <span className='item'>
                        Experience
                        </span>
                        <span className='item'>
                            {projects.experiance}
                        </span>
                    </div>
                    <div className='card'>
                        <span className='item'>
                        User Role
                        </span>
                        <span className='item'>
                            {projects.user_role}
                        </span>
                    </div>
                </div>
            </div>
        )
    }
};
export default FeaturedProjects;