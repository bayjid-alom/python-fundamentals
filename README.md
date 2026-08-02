# 🛠️ Terminal Commands


> **Open the project folder in Git Bash** before running any commands.

### ▶️ To run the Project

```bash
py main.py
```


---

# 📁 Navigation Guide

| Action | Command |
| :------ | :------ |
| 📂 Enter a folder | `cd Module-01` |
| 📂 Enter a nested folder | `cd Module-01/Problem-01` |
| ⬅️ Go back one folder | `cd ..` |
| ⬅️⬅️ Go back two folders | `cd ../..` |

---
<br>

<details>
<summary><b>💡 Quick Terminal Cheat Sheet</b></summary>

```bash
# Enter a folder
cd FolderName

# Enter nested folders
cd Folder1/Folder2

# Go back one folder
cd ..

# Go back two folders
cd ../..

# Show files and folders
ls

# Show current directory
pwd

# Run Python file
py main.py
```
</details>

---
<br>










<details>
<summary><b>♾️ Infinite Loop Note</b></summary>

### **`for` Loop**
- **Python-এর `for` loop সাধারণত Infinite Loop হয় না**, কারণ এটি নিজেই Loop Variable আপডেট করে।
- **Infinite Loop সাধারণত `while` loop-এ দেখা যায়।**

### **Example**
```python
while True:
    print("I love Python")
```

### **Infinite Loop হওয়ার দুইটি শর্ত**
1. **Condition never becomes `False`.** *(Always `True`)*
2. **Loop variable is not updated** *(No increment/decrement).*

</details>

---

