using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Despawn : MonoBehaviour {

	// Use this for initialization
	
	// Update is called once per frame
	void Update () {
		if (transform.position.y < 0) {
			SceneManager.LoadScene("Over");
		}
	}
}
