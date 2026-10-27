import json
from worker.handlers import handle_commerce
from worker.queue import Job, Worker


def main() -> None:
    jobs = [
        Job("ok-1", {"id": "a"}),
        Job("ok-2", {"id": "b"}),
        Job("bad", {"fail": True}),
    ]
    worker = Worker()
    worker.run(jobs, handle_commerce)
    print(json.dumps({
        "processed": worker.processed,
        "dead_letter": [job.name for job in worker.dead_letter],
        "domain": "commerce / inventory",
    }, indent=2))


if __name__ == "__main__":
    main()
