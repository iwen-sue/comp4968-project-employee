import { ManagerApprovalLayout } from "@/components/project/manager-approval-layout";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { useParams } from "react-router-dom";

export default function Project() {
  const navigate = useNavigate();
  const { id, name } = useParams();

  return (
    <div className="p-6">
      <div className="flex items-center gap-4 mb-6">
        <Button
          variant="outline"
          onClick={() => navigate("/")}
          className="bg-white/50"
        >
          Back to Dashboard
        </Button>
        <h1 className="text-3xl font-bold text-gradient">{name}</h1>
      </div>
      <ManagerApprovalLayout pid={id!} />
    </div>
  );
}
