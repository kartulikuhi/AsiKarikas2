using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadSceneOnInput : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if (SceneManager.GetActiveScene().name == "Title") {
			if (Input.GetAxis("Submit") == 1) {
				SceneManager.LoadScene("Play");
			}
		} else {
			if (Input.GetAxis("Submit") == 1) {
				SceneManager.LoadScene("Title");
			}
		}
	}
}
