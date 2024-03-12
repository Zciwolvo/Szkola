import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [dailyTodos, setDailyTodos] = useState([]);
  const [singleTimeTodos, setSingleTimeTodos] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [isDaily, setIsDaily] = useState(true); // Indicates whether the task is daily or single-time
  const [isNightMode, setIsNightMode] = useState(false); // Indicates whether the app is in night mode

  useEffect(() => {
    // Load tasks from localStorage on component mount
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
    // Apply night mode styles when isNightMode changes
    const body = document.body;
    if (isNightMode) {
      body.classList.add("night-mode");
    } else {
      body.classList.remove("night-mode");
    }
  }, [isNightMode]);

  const saveDailyTodos = (updatedDailyTodos) => {
    // Save daily tasks to localStorage
    localStorage.setItem("dailyTodos", JSON.stringify(updatedDailyTodos));
  };

  const saveSingleTimeTodos = (updatedSingleTimeTodos) => {
    // Save single-time tasks to localStorage
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
      };
      if (isDaily) {
        setDailyTodos([...dailyTodos, newTodo]);
        saveDailyTodos([...dailyTodos, newTodo]); // Save daily tasks after adding a new one
      } else {
        setSingleTimeTodos([...singleTimeTodos, newTodo]);
        saveSingleTimeTodos([...singleTimeTodos, newTodo]); // Save single-time tasks after adding a new one
      }
      setInputValue("");
    }
  };

  const handleDeleteTodo = (id, isDaily) => {
    if (isDaily) {
      const updatedDailyTodos = dailyTodos.filter((todo) => todo.id !== id);
      setDailyTodos(updatedDailyTodos);
      saveDailyTodos(updatedDailyTodos); // Save daily tasks after deleting one
    } else {
      const updatedSingleTimeTodos = singleTimeTodos.filter(
        (todo) => todo.id !== id
      );
      setSingleTimeTodos(updatedSingleTimeTodos);
      saveSingleTimeTodos(updatedSingleTimeTodos); // Save single-time tasks after deleting one
    }
  };

  const handleToggle = () => {
    setIsDaily(!isDaily);
  };

  const handleNightModeToggle = () => {
    setIsNightMode(!isNightMode);
  };

  return (
    <div className={`App ${isNightMode ? "night-mode" : ""}`}>
      <header className="App-header">
        <h1 className="mb-4">Todo App</h1>
        <div className="toggle-container">
          <div className="toggle">
            <label className="switch">
              <input type="checkbox" onChange={handleNightModeToggle} />
              <span className="slider round"></span>
            </label>
            <span>Night Mode</span>
          </div>
          <div className="task-toggle">
            <button
              className={`btn btn-${isDaily ? "secondary" : "primary"} mr-2`}
              onClick={handleToggle}
            >
              {isDaily ? "Daily Tasks" : "Single-time Tasks"}
            </button>
            <span className="current-task-type">
              Currently Viewing: {isDaily ? "Daily Tasks" : "Single-time Tasks"}
            </span>
          </div>
        </div>
      </header>
      <div className="container">
        <div className="input-group mb-3">
          <input
            type="text"
            className="form-control"
            placeholder="Enter a todo"
            value={inputValue}
            onChange={handleInputChange}
          />
          <button
            className="btn btn-primary"
            type="button"
            onClick={handleAddTodo}
          >
            Add Todo
          </button>
        </div>
        <div className="todos">
          {isDaily
            ? dailyTodos.map((todo) => (
                <div key={todo.id} className="todo-item">
                  <span>{todo.text}</span>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => handleDeleteTodo(todo.id, true)}
                  >
                    Delete
                  </button>
                </div>
              ))
            : singleTimeTodos.map((todo) => (
                <div key={todo.id} className="todo-item">
                  <span>{todo.text}</span>
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
