"use client";
import { getCartTotal } from "@/lib/getCartTotal";
import { groupBySkew } from "@/lib/groupBySku";
import { useCartStore } from "@/store";
import Image from "next/image";
import React from "react";
import AddToCartButton from "./AddToCartButton";
import { Button } from "./ui/button";

const Basket = () => {
  const cart = useCartStore((state) => state.cart);
  const basketTotal = getCartTotal(cart);
  const grouped = groupBySkew(cart);
  return (
    <div className="max-w-7xl mx-auto">
      <ul className="space-y-5 divide-y-2">
        {Object.keys(grouped).map((sku) => {
          const items = grouped[sku];
          return (
            <li
              key={sku}
              className="p-0 md:p-5 my-2 flex items-center justify-between"
            >
              <div className="flex flex-col md:flex-row gap-3">
                <Image
                  src={items[0].thumbnail}
                  width={70}
                  height={70}
                  alt={items[0].title}
                />
                <div>
                  <h3 className="text-lg font-semibold">{items[0].title}</h3>
                  <p className="text-sm text-gray-500">{items[0].sku}</p>
                </div>
              </div>
              <div className="flex  flex-col md:flex-row gap-2 space-x-4 pl-4">
                <AddToCartButton product={items[0]} />
                <p className="text-lg font-semibold">
                  {items.length} x ${items[0].price}
                </p>
              </div>
            </li>
          );
        })}
      </ul>

      <div className="flex flex-col justify-end ">
        <p className="font-bold text-2xl text-right text-walmart mb-5">
          Total: {basketTotal}
        </p>
        <Button
          onClick={() => {
            alert("we will add stripe for payments soon.");
          }}
          className="text-md mt-5 h-16 bg-walmart hover:bg-walmart/50"
        >
          Proceed to Checkout
        </Button>
        <Image
          className="ms-auto mt-5"
          src="/logo-stripe.png"
          alt="stripe"
          width={200}
          height={50}
        />
      </div>
    </div>
  );
};

export default Basket;
