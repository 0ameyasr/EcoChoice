"use client";
import Basket from "@/components/Basket";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { useRouter } from "next/navigation";

const BasketInterception = () => {
  const router = useRouter();

  function onDismiss() {
    router.back();
  }
  return (
    <Dialog
      open
      onOpenChange={(isOpen) => {
        if (!isOpen) onDismiss();
      }}
    >
      <DialogContent className="!h-4/5 w-full overflow-scroll px-0 md:px-5 md:max-w-3xl">
        <DialogHeader>
          <DialogTitle>Basket</DialogTitle>
          <DialogDescription>Contents of you Basket</DialogDescription>
        </DialogHeader>

        <Basket />
      </DialogContent>
    </Dialog>
  );
};

export default BasketInterception;
