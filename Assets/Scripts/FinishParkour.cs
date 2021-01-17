using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class FinishParkour : MonoBehaviour {

	public GameObject canvas;


	void OnTriggerEnter(Collider other) {
		canvas.GetComponent<Text>().text = "Congratulations! You won!";
	}
	
}
