import '../project/project.css';
import React, { Component } from 'react';

export default class DetailsPage extends Component {
    render() {
        debugger
        return (
            <div className="card">
              <h1>Welcome to Homepage</h1>
              <a href="/userinfo">Employees {this.props.match.params.id}</a>
            </div>
      )
    }
  }