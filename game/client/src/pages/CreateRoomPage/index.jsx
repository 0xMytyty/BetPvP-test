import React, { useEffect, useRef } from "react";
import Button from "../../components/Button";
import logo_img from "../../images/logo.png";
import scissors_right_hand_img from "../../images/scissors_right_hand.png";
import rock_left_hand_img from "../../images/rock_left_hand.png";
import styles from "./styles.module.css";

const CreateRoomPage = () => {
  const friendButtonRef = useRef(null); // Crea una referencia al botón de "play with friend"

  useEffect(() => {
    // Función para hacer clic en el botón de "play with friend"
    const clickFriendButton = () => {
      if (friendButtonRef.current) {
        friendButtonRef.current.click(); // Hace clic en el botón si existe
      }
    };

    // Llama a la función para hacer clic en el botón después de que la página se haya cargado completamente
    window.addEventListener("load", clickFriendButton);

    // Limpia el listener del evento cuando el componente se desmonta
    return () => {
      window.removeEventListener("load", clickFriendButton);
    };
  }, []);

  return (
    <>
      <div className={styles.left}>
        <img src={logo_img} alt="logo" className={styles.logo} />
      </div>
      <div><h1>Ola</h1></div>
      <div className={styles.right}>
        <img
          src={scissors_right_hand_img}
          alt="paper_hand"
          className={styles.paper_hand}
        />
        <img
          src={rock_left_hand_img}
          alt="rock_hand"
          className={styles.rock_hand}
        />
        <div className={styles.btn_container}>
          <Button name="play with friend" type="friend" ref={friendButtonRef} />
          <Button name="Play with stranger" type="stranger" />
        </div>
      </div>
    </>
  );
};

export default CreateRoomPage;
