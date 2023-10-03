import './App.css'
import {Header} from "./Components/Header.jsx";
import {createBrowserRouter, createRoutesFromElements, Route, RouterProvider} from "react-router-dom";
import {Signin} from "./auth/Signin.jsx";
import {Signup} from "./auth/Signup.jsx";
import {Home} from "./pages/Home.jsx";


const router = createBrowserRouter(
    createRoutesFromElements(
        <>
            <Route path="" element={<Home />}/>
            <Route path="/signin" element={<Signin/>}/>
            <Route path="/signup" element={<Signup/>}/>
        </>
    )
)

function App() {
  return (
    <RouterProvider router={router} />
  )
}

export default App
