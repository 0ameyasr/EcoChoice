import { IProduct } from "@/typings/searchTyping";

export function getCartTotal(products: IProduct[]): string {
  const total = products.reduce((acc: number, product: IProduct) => {
    return acc + product.price;
  }, 0);

  return `$ ${total.toFixed(2)}`;
}
