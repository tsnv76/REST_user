import React from 'react'
import {HashRouter, BrowserRouter, Routes, Route, Link, Navigate, useLocation} from 'react-router-dom'

import UserList from "./components/UserList";
import ProjectList from "./components/ProjectList";
import TodoList from "./components/TodoList";
import Footer from './components/Footer';
import LoginForm from "./components/LoginForm";
import TodoForm from "./components/TodoForm";
import ProjectForm from "./components/ProjectForm";
import {Box, Column, Container, HeaderLink, Row} from "./components/HeaderStyle";
import ProjectInfo from "./components/ProjectInfo";
import axios from "axios";


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
                'projects': []
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

  create_todo(text, project, user) {
      console.log('create_todo', text, project, user)
      let headers = this.get_headers()
      axios
            .post("http://127.0.0.1:8000/api/todo/", {'text': text, 'project': project, 'user': user}, {headers})
            .then(response => {
              this.get_data();
            })
            .catch(error => {
                console.log(error);
            })
    }

  delete_todo(id) {

    let headers = this.get_headers()
      console.log(id)
    axios
        .delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers})
        .then(response => {
          const todo = response.data
          //   const todo = response => {
            console.log('todo.id' + todo.id);
          this.setState({
            'todo': this.state.todo.filter((todo) => todo.id !== id)

          })
        })
        .catch(error => {
            console.log(error);
        })
    }

  create_project(name, repo_link, users) {
      console.log(name, repo_link, users)
      let headers = this.get_headers()
      axios
            .post("http://127.0.0.1:8000/api/project/", {'name': name, 'repo_link': repo_link, 'users': users}, {headers})
            .then(response => {
              this.get_data();
            })
            .catch(error => {
                console.log(error);
            })
    }


  delete_project(id) {
          console.log(id)
        let headers = this.get_headers()
        axios
            .delete(`http://127.0.0.1:8000/api/project/${id}`, {headers})
            .then(response => {
              const project = response.data
              this.setState({
                'projects': this.state.projects.filter((project) => project.id != id)

              })
            })
            .catch(error => {
                console.log(error);
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
                            <Link to="/project/create">Создание проекта</Link>
                          </Column>
                          <Column>
                            <Link to="/todo">Список заданий</Link>
                          </Column>
                          <Column>
                            <Link to="/todo/create">Создание задания</Link>
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
                    <Route exact path='/projects'   element={<ProjectList projects={this.state.projects} delete_project={(id) => this.delete_project(id)}/> } />
                    <Route exact path='/project/create'   element={<ProjectForm todo={this.state.todo} create_project={(name, repo_link, users) => this.create_todo(name, repo_link, users)}/> } />
                    <Route exact path='/todo'   element={<TodoList todo={this.state.todo} delete_todo={(id) => this.delete_todo(id)}/> } />
                    <Route exact path='/todo/create'   element={<TodoForm todo={this.state.todo} create_todo={(title, created_date, project, user) => this.create_todo(title, created_date, project, user)}/> } />
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
