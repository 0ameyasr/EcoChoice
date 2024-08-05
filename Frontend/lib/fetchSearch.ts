import { IProduct, ProductsResponse } from "../typings/searchTyping";
export async function fetchSearch(searchTerm: string) {
  try {
    const url = process.env.DUMMY_API_URL;
    const response = await fetch(`${url}/products/search?q=${searchTerm}`, {
      next: {
        revalidate: 60 * 60, // after 1 hour revalidate/refetch otherwise use cache ==> ISR
      },
    });
    console.log(response);
    const data: ProductsResponse = await response.json();

    if (!data?.products) {
      throw new Error("can't fetch data");
    }
    return data;
  } catch (err) {
    console.error(err);
  }
}

// search product by id
export async function fetchProductById(id: string) {
  try {
    const url = process.env.DUMMY_API_URL;
    const response = await fetch(`${url}/products/${id}`, {
      next: {
        revalidate: 60 * 60, // after 1 hour revalidate/refetch otherwise use cache ==> ISR
      },
    });
    console.log(response);
    const data: IProduct = await response.json();

    if (!data) {
      throw new Error("can't fetch data");
    }
    return data;
  } catch (err) {
    console.error(err);
  }
}
