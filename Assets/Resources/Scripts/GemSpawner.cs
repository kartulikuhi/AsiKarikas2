using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GemSpawner : MonoBehaviour
{
    public GameObject[] prefabs;
    // Start is called before the first frame update
    void Start() 
    {
        StartCoroutine(SpawnGem());
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    IEnumerator SpawnGem() {
        while (true) {
            int spawnGem = Random.Range(1, 3);

            if (spawnGem == 1) {
                Instantiate(prefabs[Random.Range(0, prefabs.Length)], new Vector3(26, Random.Range(-10, 10), 10), Quaternion.Euler(-90f, 180f, 0f));
            }

            yield return new WaitForSeconds(Random.Range(1, 5));
        }
    }
}
