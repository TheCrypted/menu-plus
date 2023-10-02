export const Header = ({user}) => {
	return (
		<div className="bg-zinc-900 text-white h-full bg-full grid grid-cols-[20%_40%_32%_8%]">
			<div className="transition-colors bg-zinc-700 font-bold text-3xl hover:bg-zinc-950 hover:cursor-pointer flex justify-left pl-4 items-center">
				Aman's Italian
			</div>
			<form className="h-full w-full">
				<input placeholder="Some input field goes here maybe" type="text" className="h-full w-full bg-zinc-900 focus:bg-zinc-950 transition-colors duration-300 pl-4 text-2xl outline-none"/>
			</form>
			<div className=" grid grid-cols-4">
				<div className="transition-colors flex items-center text-shadow-hover justify-center text-white font-semibold m-2 hover:bg-zinc-950 bg-zinc-500 hover:cursor-pointer rounded-lg text-2xl">Menu</div>
				<div className="transition-colors flex text-shadow-hover items-center justify-center text-slate-300 hover:text-white font-semibold m-2 hover:bg-zinc-950 rounded-lg text-2xl hover:cursor-pointer">Booking</div>
				<div className="transition-colors flex text-shadow-hover items-center justify-center text-slate-300 hover:text-white font-semibold m-2 hover:bg-zinc-950 rounded-lg text-2xl hover:cursor-pointer">About</div>
				<div className="transition-colors flex text-shadow-hover items-center justify-center text-slate-300 hover:text-white font-semibold m-2 hover:bg-zinc-950 rounded-lg text-2xl hover:cursor-pointer">Delivery</div>
			</div>
			<div className="transition-colors bg-zinc-700 flex items-center font-semibold text-3xl justify-center hover:bg-zinc-950 hover:cursor-pointer">{user && user.name}</div>
		</div>
	)
}