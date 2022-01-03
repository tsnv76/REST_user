import React from 'react'
import {HashRouter, BrowserRouter, Routes, Route, Link, Navigate, useLocation} from 'react-router-dom'

import UserList from "./components/UserList";
import ProjectList from "./components/ProjectList";
import TodoList from "./components/TodoList";
import Footer from './components/Footer';
import LoginForm from "./components/LoginForm";
import axios from 'axios'
import {Box, Column, Container, HeaderLink, Row} from "./components/HeaderStyle";
import ProjectInfo from "./components/ProjectInfo";

const NotFound = ({  }) => {
    let location = useLocation()
    return (
        <center><div>Page {location.pathname} not found</div></center>
    )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todo': [],
      'token': ''
    }
  }

  get_token(login, password) {
      axios
        .post('http://127.0.0.1:8000/api-token-auth/', {"username": login, "password": password})
        .then(response => {
          const token = response.data.token
            console.log(token)
            localStorage.setItem('token', token)
          this.setState({
            'token': token
          }, this.get_data)
        })
        .catch(error => console.log(error))
  }

  logout() {
      localStorage.setItem('token', '')
      this.setState({
          'token': ''
      }, this.get_data)
  }

  componentDidMount() {
      let token = localStorage.getItem('token')
      this.setState({
          'token': token
      }, this.get_data)
  }

  is_auth() {
      return !!this.state.token
  }

  get_headers() {
      if (this.is_auth()) {
          return {
              'Authorization': 'Token ' + this.state.token
          }
      }
      return {}
  }

  get_data() {
      let headers = this.get_headers()
    axios
        .get('http://127.0.0.1:8000/api/users/', {headers})
        .then(response => {
          const users = response.data
          this.setState({
            'users': users
          })
        })
        .catch(error => {
            console.log(error);
            this.setState({
                'users': []
            })
        })


    axios
        .get('http://127.0.0.1:8000/api/project/', {headers})
        .then(response => {
          const projects = response.data
          this.setState({
            'projects': projects
          })
        })
        .catch(error => {
            console.log(error);
            this.setState({
                'project': []
            })
        })

    axios
        .get('http://127.0.0.1:8000/api/todo/', {headers})
        .then(response => {
          const todo = response.data
          this.setState({
            'todo': todo
          })
        })
        .catch(error => {
            console.log(error);
            this.setState({
                'todo': []
            })
        })
  }

  render () {
    return (
        <div>

            <BrowserRouter>
                <nav>
                    {/*<Header />*/}
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
                          <Column>
                              {/*<Link to="/login">Login</Link>*/}
                            { this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to="/login">Login</Link> }
                          </Column>
                        </Row>
                      </Container>
                    </Box>
                </nav>
                <Routes>
                    <Route exact path='/' element={<UserList users={this.state.users} /> } />
                    <Route exact path='/projects'   element={<ProjectList projects={this.state.projects} /> } />
                    <Route exact path='/todo'   element={<TodoList todo={this.state.todo} /> } />
                    <Route exact path='/login'   element={<LoginForm  get_token={(login, password) => this.get_token(login, password)}/> } />
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
