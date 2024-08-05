import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";
import { IProduct } from "./typings/searchTyping";

export interface CartState {
  cart: IProduct[];
  addToCart: (product: IProduct) => void;
  removeFromCart: (product: IProduct) => void;
}

export const useCartStore = create<CartState>()(
  devtools(
    persist(
      // create like a cookie for the store ==> keep the data even after refresh
      (set, get) => ({
        cart: [],
        addToCart: (product: IProduct) => {
          set((state) => ({ cart: [...state.cart, product] }));
        },
        // removeFromCart: (product: IProduct) => {
        //   set((state) => ({
        //     cart: state.cart.filter((item, index) => {
        //       if (item.id === product.id) {
        //         // Remove only the first occurrence of the product
        //         state.cart.splice(index, 1);

        //         if (state.cart.length != 0) return true;
        //       }
        //     }),
        //   }));
        // },

        removeFromCart: (product) => {
          const productToRemove = get().cart.findIndex(
            (p) => p.sku === product.sku
          );

          set((state) => {
            const newCart = [...state.cart];
            newCart.splice(productToRemove, 1);
            return { cart: newCart };
          });
        },
      }),
      {
        name: "shopping-cart-storage",
      }
    )
  )
);
