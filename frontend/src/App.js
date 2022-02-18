import logo from './logo.svg';
import './App.css';
import React from 'react';


import FeaturedProjects from './views/components/project/project.jsx'
import FeaturedProject from './views/components/project/project.jsx'

import Home from './views/components/home/home.jsx'
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="wrapper">
      <BrowserRouter>
        <Routes>
          <Route path='/userinfo/:id' element={<FeaturedProjects/>} />
          <Route path='/userinfo/' element={<FeaturedProjects/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;