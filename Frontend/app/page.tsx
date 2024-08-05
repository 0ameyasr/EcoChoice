import GridOption from "@/components/GridOption";

export default function Home() {
  return (
    <main className="flex-1">
      <div className="grid grid-col-1 gap-3 p-3 grid-flow-row-dense md:grid-cols-4">
        <GridOption
          title="Sweet gifts for your loved ones"
          image="/gift.webp"
          query="red"
          className="bg-purple-300 h-full md:h-32"
        />
        {/* https://links.papareact.com/ */}
        <GridOption
          title="Shop Wardrobe Essentials"
          image="/wardrobes.webp"
          className="bg-blue-300 col-span-2 row-span-2"
          query="Wardrobe"
        />
        <GridOption
          title="Shop Home"
          image="/home.webp"
          className="bg-pink-200 row-span-2"
          query="home"
        />
        <GridOption
          title="Shop Electronics"
          image="/Electronics.webp"
          className="bg-yellow-100 h-64"
          query="phone"
        />
        <GridOption
          title="Shop Toys"
          image="/Toys.webp"
          className="bg-green-100 h-64 col-span-2"
          query="game"
        />
        <GridOption
          title="All you need to match your style"
          image="/style.webp"
          className="bg-red-100 col-span-2 row-span-2"
          query="style"
        />
        <GridOption
          title="Shop Gadgets"
          image="/Gadgets.webp"
          className="bg-orange-100 h-64"
          query="Gadgets"
        />
        <GridOption
          title="Shop Beauty"
          image="/Beauty.webp"
          className="bg-blue-100 h-64"
          query="makeup"
        />
        <GridOption
          title="Shop Sports"
          image="/Sports.webp"
          className="bg-blue-100 h-64"
          query="Sports"
        />
        <GridOption
          title="Enjoy Free Shipping"
          image="/joy.webp"
          className="bg-rose-100 h-64"
          query="joy"
        />
        <GridOption
          title="Flash Deals"
          image="/8ko.webp"
          className="bg-orange-100 h-64 col-span-2"
          query="deal"
        />
      </div>
    </main>
  );
}
