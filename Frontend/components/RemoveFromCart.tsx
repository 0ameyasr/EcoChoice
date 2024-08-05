"use client";
import { useCartStore } from "@/store";
import React from "react";
import { IProduct } from "@/typings/searchTyping";
import { Button } from "./ui/button";
const RemoveFromCart = ({ product }: { product: IProduct }) => {
  const removeFromCart = useCartStore((state) => state.removeFromCart);
  const handleRemove = () => {
    removeFromCart(product);
  };
  return (
    <Button onClick={handleRemove} className="bg-walmart hover:bg-walmart/50">
      -
    </Button>
  );
};

export default RemoveFromCart;
