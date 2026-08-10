from collections import namedtuple
from typing import List, Tuple

# ==========================================
# SCENARIO 1: Backend Development (FastAPI / SQL)
# ==========================================
# When fetching rows from a raw SQL query using psycopg2, 
# returning tuples like (1, "AI Engineer", True) can get confusing to read.
# A namedtuple allows you to access columns by attribute name, just like a Pydantic model or SQLAlchemy object!

# 1. Define the namedtuple schema
DBPostRecord = namedtuple('DBPostRecord', ['id', 'title', 'content', 'published'])

# 2. Simulate raw database rows fetched from Postgres
raw_database_rows = [
    (1, "FastAPI Backend Architecture", "Building robust APIs with Python", True),
    (2, "YOLOv8 Computer Vision", "Real-time object detection", True),
    (3, "Draft Article", "Unpublished internal notes", False)
]

def process_database_rows(rows: List[Tuple]) -> List[DBPostRecord]:
    """Converts raw database tuples into clean, attribute-accessible namedtuples."""
    processed_posts = []
    for row in rows:
        # Unpack the tuple into our namedtuple structure
        post = DBPostRecord._make(row)
        processed_posts.append(post)
    return processed_posts


# ==========================================
# SCENARIO 2: Computer Vision (OpenCV & YOLO)
# ==========================================
# When YOLO detects objects in an image or webcam feed, 
# it returns bounding box coordinates (xmin, ymin, xmax, ymax), confidence scores, and class IDs.

# 1. Define a namedtuple for object detection bounding boxes
BoundingBox = namedtuple('BoundingBox', ['xmin', 'ymin', 'xmax', 'ymax', 'confidence', 'class_name'])

def filter_high_confidence_detections(detections: List[Tuple], threshold: float = 0.75) -> List[BoundingBox]:
    """Filters raw YOLO detections and maps them to clean BoundingBox namedtuples."""
    valid_detections = []
    
    for det in detections:
        # det format: (xmin, ymin, xmax, ymax, confidence, class_id)
        xmin, ymin, xmax, ymax, conf, class_id = det
        
        # Map class ID to name
        name = "person" if class_id == 0 else "car"
        
        if conf >= threshold:
            box = BoundingBox(xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax, confidence=conf, class_name=name)
            valid_detections.append(box)
            
    return valid_detections


# ==========================================
# SCENARIO 3: Configuration Management
# ==========================================
# Instead of loose global variables or messy dictionaries for app settings,
# namedtuples provide immutable, read-only configuration objects.

AppConfig = namedtuple('AppConfig', ['host', 'port', 'debug_mode', 'model_path'])

def load_environment_config() -> AppConfig:
    # Simulating loading configuration settings
    return AppConfig(
        host="127.0.0.1",
        port=8000,
        debug_mode=True,
        model_path="yolov8n.pt"
    )


# ==========================================
# MAIN EXECUTION & DEMONSTRATION
# ==========================================
if __name__ == "__main__":
    print("--- 1. DATABASE NAMEDTUPLE DEMO ---")
    posts = process_database_rows(raw_database_rows)
    for p in posts:
        # Accessing fields by name instead of ugly index numbers like p[1]!
        if p.published:
            print(f"Published Post [{p.id}]: {p.title} -> {p.content}")

    print("\n--- 2. COMPUTER VISION (YOLO) DEMO ---")
    # Simulated raw model outputs: (xmin, ymin, xmax, ymax, confidence, class_id)
    raw_yolo_outputs = [
        (10, 20, 100, 200, 0.92, 0),  # Person
        (150, 220, 300, 400, 0.45, 1), # Car (low confidence)
        (50, 60, 120, 250, 0.88, 0)    # Person
    ]
    
    detected_objects = filter_high_confidence_detections(raw_yolo_outputs, threshold=0.7)
    for obj in detected_objects:
        # Clean dot-notation access!
        print(f"Detected {obj.class_name} with {obj.confidence * 100:.1f}% confidence at box [{obj.xmin}, {obj.ymin}]")

    print("\n--- 3. CONFIGURATION DEMO ---")
    config = load_environment_config()
    print(f"Server starting on {config.host}:{config.port} (Debug: {config.debug_mode})")
    print(f"Active AI Model: {config.model_path}")
    
    # BONUS: Namedtuples are immutable (read-only)! 
    # Attempting to change a value like 'config.port = 9000' will throw an AttributeError, 
    # which is fantastic for protecting configuration data from accidental bugs.