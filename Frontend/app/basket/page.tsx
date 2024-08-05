import Basket from "@/components/Basket";
import { ShoppingCartIcon } from "lucide-react";
import React from "react";

const BasketPage = () => {
  return (
    <div className="w-full p-10 max-w-7xl mx-auto">
      <div className="flex items-center space-x-2">
        <ShoppingCartIcon size={32} />
        <h1 className="text-3xl font-regular">Your Cart</h1>
      </div>
      <p className="mt-2 mb-5">
        Review the items in your cart and proceed to checkout.
      </p>

      <Basket />
    </div>
  );
};

export default BasketPage;
