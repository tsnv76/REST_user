import React from 'react'
import {HashRouter, BrowserRouter, Routes, Route, Link, Navigate} from 'react-router-dom'
// import Header from './components/Header';
import UserList from "./components/UserList";
import ProjectList from "./components/ProjectList";
import TodoList from "./components/TodoList";
import Footer from './components/Footer';
import axios from 'axios'
import {Box, Column, Container, HeaderLink, Row} from "./components/HeaderStyle";
import ProjectInfo from "./components/ProjectInfo";

const NotFound = ({  }) => {
    return (
        <div>Page  not found</div>
    )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todo': []
    }
  }

  componentDidMount() {
    axios
        .get('http://127.0.0.1:8000/api/users/')
        .then(response => {
          const users = response.data
          this.setState({
            'users': users
          })
        })
        .catch(error => console.log())


    axios
        .get('http://127.0.0.1:8000/api/project/')
        .then(response => {
          const projects = response.data
          this.setState({
            'projects': projects
          })
        })
        .catch(error => console.log())

    axios
        .get('http://127.0.0.1:8000/api/todo/')
        .then(response => {
          const todo = response.data
          this.setState({
            'todo': todo
          })
        })
        .catch(error => console.log())
  }

  render () {
    return (
        <div>
            <BrowserRouter>
                <nav>
                    <Box>
                        <Container>
                        <Row>
                          <Column>
                            <Link to="/">Пользователи</Link>
                          </Column>
                          <Column>
                            <Link to="/projects">Проекты</Link>
                          </Column>
                          <Column>
                            <Link to="/todo">Список заданий</Link>
                          </Column>
                        </Row>
                      </Container>
                    </Box>
                </nav>
                <Routes>
                    <Route exact path='/' element={<UserList users={this.state.users} /> } />
                    <Route exact path='/projects'   element={<ProjectList projects={this.state.projects} /> } />
                    <Route exact path='/todo'   element={<TodoList todo={this.state.todo} /> } />
                    <Route path="/users" element={<Navigate to="/" />} />
                    <Route path='/project/:id'   element={<ProjectInfo projects={this.state.projects} /> } />
                    <Route path="*" element={<NotFound /> } />
                </Routes>
            </BrowserRouter>
            <Footer />
        </div>
    )
  }
}

export default App;
