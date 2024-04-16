import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App2.css";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [dailyTodos, setDailyTodos] = useState([]);
  const [singleTimeTodos, setSingleTimeTodos] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [isDaily, setIsDaily] = useState(true);
  const [isNightMode, setIsNightMode] = useState(false);

  useEffect(() => {
    const savedDailyTodos = JSON.parse(localStorage.getItem("dailyTodos"));
    const savedSingleTimeTodos = JSON.parse(
      localStorage.getItem("singleTimeTodos")
    );

    if (savedDailyTodos && savedDailyTodos.length > 0) {
      setDailyTodos(savedDailyTodos);
    }

    if (savedSingleTimeTodos && savedSingleTimeTodos.length > 0) {
      setSingleTimeTodos(savedSingleTimeTodos);
    }
  }, []);

  useEffect(() => {
    const body = document.body;
    if (isNightMode) {
      body.classList.add("night-mode");
    } else {
      body.classList.remove("night-mode");
    }
  }, [isNightMode]);

  useEffect(() => {
    const resetDailyTasks = setInterval(() => {
      const currentTime = new Date().getTime();
      const updatedDailyTodos = dailyTodos.map((todo) => {
        if (todo.done && currentTime - todo.timestamp >= 24 * 60 * 60 * 1000) {
          return { ...todo, done: false };
        }
        return todo;
      });
      setDailyTodos(updatedDailyTodos);
      localStorage.setItem("dailyTodos", JSON.stringify(updatedDailyTodos));
    }, 1000);

    return () => clearInterval(resetDailyTasks);
  }, [dailyTodos]);

  const saveDailyTodos = (updatedDailyTodos) => {
    localStorage.setItem("dailyTodos", JSON.stringify(updatedDailyTodos));
  };

  const saveSingleTimeTodos = (updatedSingleTimeTodos) => {
    localStorage.setItem(
      "singleTimeTodos",
      JSON.stringify(updatedSingleTimeTodos)
    );
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleAddTodo = () => {
    if (inputValue.trim() !== "") {
      const newTodo = {
        id: dailyTodos.length + singleTimeTodos.length + 1,
        text: inputValue,
        done: false,
        timestamp: new Date().getTime(),
      };
      if (isDaily) {
        setDailyTodos([...dailyTodos, newTodo]);
        saveDailyTodos([...dailyTodos, newTodo]);
      } else {
        setSingleTimeTodos([...singleTimeTodos, newTodo]);
        saveSingleTimeTodos([...singleTimeTodos, newTodo]);
      }
      setInputValue("");
    }
  };

  const handleDeleteTodo = (id, isDaily) => {
    if (isDaily) {
      const updatedDailyTodos = dailyTodos.filter((todo) => todo.id !== id);
      setDailyTodos(updatedDailyTodos);
      saveDailyTodos(updatedDailyTodos);
    } else {
      const updatedSingleTimeTodos = singleTimeTodos.filter(
        (todo) => todo.id !== id
      );
      setSingleTimeTodos(updatedSingleTimeTodos);
      saveSingleTimeTodos(updatedSingleTimeTodos);
    }
  };

  const handleToggle = () => {
    setIsDaily(!isDaily);
  };

  const handleNightModeToggle = () => {
    setIsNightMode(!isNightMode);
  };

  const handleMarkAsDone = (id, isDaily) => {
    if (isDaily) {
      const updatedDailyTodos = dailyTodos.map((todo) =>
        todo.id === id ? { ...todo, done: !todo.done } : todo
      );
      setDailyTodos(updatedDailyTodos);
      saveDailyTodos(updatedDailyTodos);
    } else {
      const updatedSingleTimeTodos = singleTimeTodos.map((todo) =>
        todo.id === id ? { ...todo, done: !todo.done } : todo
      );
      setSingleTimeTodos(updatedSingleTimeTodos);
      saveSingleTimeTodos(updatedSingleTimeTodos);
    }
  };

  return (
    <div
      className={`App ${
        isNightMode ? "bg-gray-900 text-white" : "bg-gray-100"
      }`}
    >
      <header className="App-header">
        <h1 className="text-2xl mb-4">Todo App (Igor Gawłowicz)</h1>
        <div className="toggle-container flex justify-between items-center">
          <div className="toggle flex items-center">
            <label className="switch">
              <input type="checkbox" onChange={handleNightModeToggle} />
              <span className="slider round"></span>
            </label>
            <span>Night Mode</span>
          </div>
          <div className="task-toggle">
            <button
              class="bg-transparent hover:bg-blue-500 text-grey-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
              onClick={handleToggle}
            >
              {isDaily ? "Daily Tasks" : "Single-time Tasks"}
            </button>
          </div>
        </div>
      </header>
      <div className="container mx-auto p-4">
        <div className="input-group flex mb-3">
          <input
            type="text"
            className="form-control rounded-md px-3 py-2 focus:outline-none focus:ring-blue-500 focus:ring-1"
            placeholder="Enter a todo"
            value={inputValue}
            onChange={handleInputChange}
          />
          <button
            class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-black py-2 px-4 border border-blue-500 hover:border-transparent rounded"
            type="button"
            onClick={handleAddTodo}
          >
            Add Todo
          </button>
        </div>
        <div className="todos">
          {isDaily
            ? dailyTodos.map((todo) => (
                <div
                  key={todo.id}
                  className="todo-item p-3 bg-white rounded-md shadow-sm flex justify-between items-center"
                >
                  <span
                    className={`text-lg ${todo.done ? "line-through" : ""}`}
                    onClick={() => handleMarkAsDone(todo.id, true)}
                  >
                    {todo.text}
                  </span>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleDeleteTodo(todo.id, true)}
                  >
                    Delete
                  </button>
                </div>
              ))
            : singleTimeTodos.map((todo) => (
                <div
                  key={todo.id}
                  className="todo-item p-3 bg-white rounded-md shadow-sm flex justify-between items-center"
                >
                  <span
                    className={`text-lg ${todo.done ? "line-through" : ""}`}
                    onClick={() => handleMarkAsDone(todo.id, false)}
                  >
                    {todo.text}
                  </span>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleDeleteTodo(todo.id, false)}
                  >
                    Delete
                  </button>
                </div>
              ))}
        </div>
      </div>
    </div>
  );
}

export default App;
