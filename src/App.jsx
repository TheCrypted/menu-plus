import './App.css'
import {Header} from "./Components/Header.jsx";

function App() {

  return (
    <div className="bg-slate-900 h-full w-full grid grid-rows-[8%_92%]">
        <Header user={{name: "Aman"}} />
        Hello
    </div>
  )
}

export default App
