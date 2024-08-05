"use client";
import { useCartStore } from "@/store";
import { IProduct } from "@/typings/searchTyping";
import React from "react";
import { Button } from "./ui/button";
import RemoveFromCart from "./RemoveFromCart";

const AddToCartButton = ({ product }: { product: IProduct }) => {
  const [cart, addToCart] = useCartStore((state) => [
    state.cart,
    state.addToCart,
  ]);

  const howManyInCart = cart.filter(
    (item) => item.meta.barcode === product.meta.barcode
  ).length; // or id or SKU

  console.log({ cart, howManyInCart });
  const handleAdd = () => {
    addToCart(product);
  };

  if (howManyInCart > 0) {
    return (
      <div className="flex space-x-5 items-center">
        <RemoveFromCart product={product} />
        <span>{howManyInCart}</span>
        <Button className="bg-walmart hover:bg-walmart/50" onClick={handleAdd}>
          +
        </Button>
      </div>
    );
  }

  return <Button onClick={handleAdd}>Add to Cart</Button>;
};

export default AddToCartButton;
