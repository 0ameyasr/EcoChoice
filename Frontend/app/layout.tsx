import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Walmart 3.0 Clone",
  description: "Airakaz - Walmart 3.0 Clone",
};

export default function RootLayout({
  children,
  modal,
}: Readonly<{
  children: React.ReactNode;
  modal: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {/* header */}
        <Header />
        {modal}
        <div>{children}</div>
      </body>
    </html>
  );
}
