import './App.css';

async function TodoList() {
  fetch('http://127.0.0.1:8001/todo/api/todos').then(
    resp => console.log(resp)
  )
}

function App() {
  TodoList()
  return (
    <div className="App">
      <p>Todos</p>
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
