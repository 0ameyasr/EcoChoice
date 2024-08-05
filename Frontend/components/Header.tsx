"use client";
import { useCartStore } from "@/store";
import {
  Grid2X2,
  Heart,
  LayoutGrid,
  Search,
  ShoppingCart,
  User,
} from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { FormEvent } from "react";
import { getCartTotal } from "@/lib/getCartTotal";
const Header = () => {
  const router = useRouter();
  const cart = useCartStore((state) => state.cart);
  const total = getCartTotal(cart);

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    //stop the page from refreshing
    e.preventDefault();
    console.log("searching...");

    const input = e.currentTarget.input.value;
    router.push(`/search?q=${input}`);
  };

  return (
    <header className="flex flex-col md:flex-row bg-walmart items-center px-10 py-7 space-x-0  md:space-x-5 space-y-5 md:space-y-0">
      <Link href="/" className="">
        <Image
          src="/Walmart_logo.svg"
          alt="Walmart Logo"
          width={160}
          height={40}
        />
      </Link>
      <form
        onSubmit={handleSubmit}
        className="flex items-center bg-white rounded-full w-full flex-1"
      >
        <input
          className="flex-1 px-4 rounded-full outline-none placeholder:text-sm text-black"
          type="text"
          name="input"
          placeholder="Search everything..."
        />
        <button>
          <Search className="rounded-full h-10 px-2 w-10 bg-yellow-400 cursor-pointer" />
        </button>
      </form>
      <div className="flex space-x-5 ">
        <Link
          href="/"
          className="hidden xl:flex text-white font-bold items-center space-x-2 text-sm"
        >
          <Grid2X2 size={20} />
          <p>Departments</p>
        </Link>
        <Link
          href="/"
          className="hidden xl:flex text-white font-bold items-center space-x-2 text-sm"
        >
          <LayoutGrid size={20} />
          <p>Services</p>
        </Link>
        <Link
          href="/"
          className="flex text-white font-bold items-center space-x-2 text-sm"
        >
          <Heart size={20} />
          <div>
            <p className="text-xs font-extralight">Reorder</p>
            <p>My Items</p>
          </div>
        </Link>
        <Link
          href="/"
          className="flex text-white font-bold items-center space-x-2 text-sm"
        >
          <User size={20} />
          <div>
            <p className="text-xs font-extralight">Sign In</p>
            <p>Account</p>
          </div>
        </Link>
        <Link
          href="/basket"
          className="flex text-white font-bold items-center space-x-2 text-sm"
        >
          <ShoppingCart size={20} />
          <div>
            <p className="text-xs font-extralight">
              {cart.length ? `${cart?.length} items` : "Your cart is empty"}
            </p>
            <p>{total}</p>
          </div>
        </Link>
      </div>
    </header>
  );
};

export default Header;
