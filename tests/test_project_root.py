import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.project_root import find_project_root


class ProjectRootResolutionTests(unittest.TestCase):
    def test_find_project_root_from_notebook_directory(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            repo = Path(tmp_dir)
            (repo / "notebooks").mkdir()
            (repo / "src").mkdir()
            (repo / "generate_data.py").write_text("print('ok')\n", encoding="utf-8")

            self.assertEqual(find_project_root(repo / "notebooks"), repo)


if __name__ == "__main__":
    unittest.main()
