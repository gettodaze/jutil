import './App.css';
import React from 'react';
var ReactDOM = require('react-dom')

function formatTodo(todo) {
  // note: we are adding a key prop here to allow react to uniquely identify each
  // element in this array. see: https://reactjs.org/docs/lists-and-keys.html
  return <><input type="checkbox" key={todo.id} checked={todo.completed}></input><label>{todo.description}</label></>
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
    fetch('http://127.0.0.1:8001/todo/api/todos')
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: result.items
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
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <ul>{items.map(formatTodo)}</ul>
      );
    }
  }
}

const root = ReactDOM.client.createRoot(
  document.getElementById('root')
);

function App() {
  return (
    <div className="App">
      {root.render(TodoList)}
      <form>
        <label>
          Add Todo:
    <input type="text" name="name" />
        </label>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}
export default App;
