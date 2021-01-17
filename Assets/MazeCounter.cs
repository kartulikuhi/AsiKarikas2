using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MazeCounter : MonoBehaviour {

	// Use this for initialization
	private Text txt;

	private int mazeCount;
	void Awake () {
		txt = GetComponent<Text>();
		mazeCount = DontDestroy.mazeCount;
		txt.text = "Maze counter: " + mazeCount.ToString();
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
