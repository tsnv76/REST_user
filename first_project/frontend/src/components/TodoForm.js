import React from 'react'

class TodoForm extends React.Component {
    constructor(prop) {
        super(prop)
        this.state = {
            'text': '',
            'project': [],
            'user': [],
        }
    }


    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
            }
        )
    }

    handleUserChange(event) {
        if (!event.target.selectedOptions) {
            return;
        }

        let user =[]
        for (let i=0; i < event.target.selectedOptions.length; i++) {
            user.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            ['user']: user
            }
        )
    }

    handleSubmit(event) {
        // console.log('handleSubmit', this.state.text, this.state.project, this.state.user)
        this.props.create_todo(this.state.text, this.state.project, this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="text" placeholder="title" value={this.state.text}
                       onChange={(event) => this.handleChange(event)}/>
                <input type="text" name="project" placeholder="project" value={this.state.project}
                       onChange={(event) => this.handleChange(event)}/>
                <input type="text" name="user" placeholder="user" value={this.state.user}
                       onChange={(event) => this.handleChange(event)}/>
                {/*<select  name="project" onChange={(event) => this.handleChange(event)}>*/}
                {/*    {this.props.project.map((users) =><option value={project.id}>{project.name}</option>)}*/}
                {/*</select>*/}
                {/*<select  name="user" onChange={(event) => this.handleUserChange(event)}>*/}
                {/*    {this.props.users.map((user) =><option value={user.id}>{user.email}</option>)}*/}
                {/*</select>*/}
                <input type="submit" value="Create" />
            </form>
        )
    }
}

export default TodoForm;

