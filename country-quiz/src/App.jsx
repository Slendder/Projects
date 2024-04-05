import './App.css'

function App() {
    fetch('https://restcountries.com/v3.1/all')
        .then(response => response.json())
        .then(data => {
            console.log(data[1])
        })
        .catch(error => {
            console.log(error)
        })
  return (
    <div className={"container"}>
      <h1>sds</h1>
    </div>
  )
}

export default App
