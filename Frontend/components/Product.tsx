import { IProduct } from "@/typings/searchTyping";
import Image from "next/image";
import Link from "next/link";
import React from "react";
import { Badge } from "./ui/badge";

const Product = ({ product }: { product: IProduct }) => {
  return (
    <Link
      href={`/product/${product.id}`}
      className="flex flex-col relative border rounded-md h-full p-5"
    >
      <Image
        width={300}
        height={300}
        src={product.images[0]}
        alt={product.title}
        className="w-full h-48 object-scale-down"
      />
      <h3 className="text-xl font-semibold mt-2">{product.title}</h3>
      <p className="text-lg text-neutral-600 font-semibold">${product.price}</p>
      <Badge className="w-fit absolute top-2 right-2">
        {product.discountPercentage}% OFF
      </Badge>
    </Link>
  );
};

export default Product;
