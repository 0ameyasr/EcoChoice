import AddToCartButton from "@/components/AddToCartButton";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";
import { fetchProductById } from "@/lib/fetchSearch";
import Image from "next/image";
import { notFound } from "next/navigation";
import React from "react";

interface Props {
  params: {
    id: string;
  };
}
const delay = (ms: any) => new Promise((res) => setTimeout(res, ms));

const ProductPage = async ({ params }: Props) => {
  if (isNaN(Number(params.id))) notFound();
  const product = await fetchProductById(params.id);
  if (!product) notFound();

  await delay(1000);
  return (
    <div className="fp-4 lg:p-10 flex flex-col lg:flex-row w-full">
      <div className="hidden lg:inline space-y-4">
        {product?.images.map((image, index) => (
          <Image
            key={index}
            src={image}
            width={90}
            height={90}
            alt={product.title + " image " + index}
            className="border rounded-lg"
          />
        ))}
      </div>
      <Carousel
        opts={{
          loop: true,
        }}
        className="w-3/5 mb-10 lg:mb-0  self-start flex items-center max-w-xl mx-auto lg:mx-20"
      >
        <CarouselContent>
          {product?.images.map((image, index) => (
            <CarouselItem key={index + "product"}>
              <div className="p-1">
                <div className="flex aspect-square items-center justify-center p-2 relative">
                  <Image
                    src={image}
                    width={800}
                    height={800}
                    alt={product.title + " image " + index}
                  />
                </div>
              </div>
            </CarouselItem>
          ))}
        </CarouselContent>
        <CarouselPrevious />
        <CarouselNext />
      </Carousel>

      <div className="flex flex-col space-y-4 p-4">
        <h1 className="text-2xl font-semibold">
          {product?.title} - {product?.sku}
        </h1>
        <div className="space-x-2">
          {product?.tags.map((tag, index) => (
            <Badge key={index} className="text-sm font-light" variant="outline">
              {tag}
            </Badge>
          ))}
        </div>
        <p className="text-lg font-light">{product?.description}</p>
        <p className="text-yellow-500 text-sm">
          {product?.rating} ⭐{" "}
          <span className="text-gray-400 ml-2">
            ({product?.reviews.length} reviews)
          </span>
        </p>
        <p className="text-2xl font-semibold mt-2">Price: ${product?.price}</p>
        <AddToCartButton product={product} />

        <hr />

        {product?.reviews && (
          <div className="flex flex-col space-y-4 p-4">
            {product.reviews.map((review, index) => (
              <div key={index} className="flex flex-col space-y-2">
                <h3 className="text-md font-semibold">{review.comment}</h3>

                <div className="flex flex-col md:flex-row space-x-2 ms-3">
                  <p className="text-yellow-500 text-sm">{review.rating} ⭐ </p>
                  <div>
                    <span>{review.reviewerName}</span>
                    &nbsp;-
                    <span>{review.reviewerEmail}</span>
                  </div>
                </div>
                <div className="flex space-x-2  ms-3">
                  <span>{review.date}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductPage;
