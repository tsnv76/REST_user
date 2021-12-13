import React from 'react'
import Header from './components/Header';
import UserList from "./components/UserList";
import Footer from './components/Footer';
import axios from 'axios'


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
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
  }

  render () {
    return (
        <div>

            <Header />
            <UserList users={this.state.users} ></UserList>
            <Footer />
        </div>
    )
  }
}

export default App;
