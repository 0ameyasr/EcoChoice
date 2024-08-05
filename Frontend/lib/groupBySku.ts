import { IProduct } from "@/typings/searchTyping";

export function groupBySkew(products: IProduct[]): Record<string, IProduct[]> {
  return products?.reduce(
    (acc: Record<string, IProduct[]>, currentProduct: IProduct) => {
      if (!acc[currentProduct.sku]) {
        acc[currentProduct.sku] = [];
      }
      acc[currentProduct.sku].push(currentProduct);
      return acc;
    },
    {}
  );
}
