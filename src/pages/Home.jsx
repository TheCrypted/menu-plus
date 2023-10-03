import {Header} from "../Components/Header.jsx";

export function Home() {
	return (
		<div className="bg-slate-900 h-full w-full grid grid-rows-[8%_92%]">
			<Header user={{name: "Aman"}} />
			Hello
		</div>
	)
}