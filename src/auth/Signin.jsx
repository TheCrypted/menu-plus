import {Link, useNavigate} from "react-router-dom";
import {useRef} from "react";

export const Signin = () => {
	const usernameRef = useRef(null);
	const passwordRef = useRef(null);
	const navigate = useNavigate();

	return (
		<div className="w-full h-full bg-zinc-800 flex items-center justify-center text-white">
			<div className="w-1/3 h-2/5 bg-zinc-900 rounded-xl shadow-xl hover:shadow-2xl transition duration-300">
				<form className="h-full w-full rounded-xl p-4 pt-0 grid grid-rows-[30%_25%_25%_20%]">
					<div className="flex items-center font-bold justify-center text-4xl">Meet + <Link className="font-light w-4/6 flex justify-end text-sm hover:underline" to="/signup">Not an Existing User? Signup</Link></div>
					<input ref={usernameRef} required placeholder="Enter username" className=" p-3 text-2xl font-semibold focus:outline-none bg-zinc-800 mb-2 rounded-lg" type="text"/>
					<input ref={passwordRef} required placeholder="Enter password" className=" p-3 text-2xl font-semibold focus:outline-none bg-zinc-800 mb-2 rounded-lg" type="password"/>
					<button className="bg-slate-900 hover:bg-slate-800 font-bold text-2xl rounded-lg" type="submit" onClick={async (e)=>{
						e.preventDefault();
						let response = await fetch("http://localhost:8000/accounts/login/", {
							method: "POST",
							headers: {
								"content-type": "application/json",
							},
							body: JSON.stringify({
								email: usernameRef.current.value,
								username: usernameRef.current.value.split("@")[0],
								password: passwordRef.current.value
							})
						})
						let resp = await response.json()
						if(response.ok){
							// localStorage.setItem("token", resp.token) Set the jsonwebtoken response in localstorage
							navigate("/")
						} else {
							alert(resp.message)
						}
					}}>Submit
					</button>
				</form>
			</div>
		</div>
	)
}