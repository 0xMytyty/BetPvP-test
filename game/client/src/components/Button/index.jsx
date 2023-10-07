import { useContext, forwardRef } from "react";
import { SocketContext } from "../../context/SocketContext";
import btn_background_img from "../../images/btn_background.png";
import styles from "./styles.module.css";

const Button = forwardRef(({ name, type }, ref) => {
  const { socket, navigate } = useContext(SocketContext);

  const handleChange = (type) => {
    socket.emit("room:create", { type }, (err, roomId) => {
      // Agrega un console.log para imprimir el roomId
      console.log(`roomId:${roomId}`);

      navigate(`/room/${roomId}`);
    });
  };

  return (
    <button className={styles.btn} onClick={() => handleChange(type)} ref={ref}>
      <img
        src={btn_background_img}
        alt="btn_background_img"
        className={styles.btn_background_img}
      />
      {name}
    </button>
  );
});

export default Button;

