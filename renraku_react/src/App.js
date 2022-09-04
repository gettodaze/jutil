import './App.css';
import React from 'react';
var ReactDOM = require('react-dom')

function formatTodo(todo) {
  // note: we are adding a key prop here to allow react to uniquely identify each
  // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
  return <p><input type="checkbox" key={todo.id} checked={todo.completed}></input><label>{todo.description}</label></p>
}


class TodoList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentDidMount() {
    console.log("Component Mounted")
    fetch('http://127.0.0.1:8000/todo/api/todos')
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: result
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;
    console.log(this.state)
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <ul align="left">{items.map(formatTodo)}</ul>
      );
    }
  }
}

function newTodo(title) {
  fetch('http://127.0.0.1:8000/todo/api/todos',
    {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: title
      })
    });
}

function App() {
  return (
    <div className="App">
      <TodoList />
      <form>
        <label>
          Add Todo:
    <input type="text" name="name" onSubmit="newTodo()" />
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}
export default App;
