from enum import Enum
from typing import List, Optional

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class SourceLicense:
    BASIC: str = "basic"
    STANDARD: str = "standard"
    STANDARD_PLUS: str = "standard+"
    ADVANCED: str = "advanced"


class EntryResult:
    NEW: str = "new"
    REINIT: str = "reinit"
    EXACT: str = "exact"
    HA: str = "ha"
    JUNK: str = "advanced"
    NM: str = "nm"
    DET: str = "dev"


class Sources(APIBase):
    def create(
        self,
        name: str,
        license_type: str = SourceLicense.BASIC,
        identify_facesize_threshold: int = 7000,
        use_pps_time: bool = False,
        manual_create_facesize_threshold: int = 25000,
        manual_create_on_ha: bool = False,
        manual_create_on_junk: bool = False,
        manual_identify_asm: bool = True,
        auto_create_persons: bool = False,
        auto_create_facesize_threshold: int = 25000,
        auto_create_check_blur: bool = True,
        auto_create_check_exposure: bool = True,
        auto_create_on_ha: bool = False,
        auto_create_on_junk: bool = False,
        auto_check_face_angle: bool = True,
        auto_check_liveness: bool = False,
        auto_create_liveness_only: bool = True,
        auto_identify_asm: bool = True,
        store_images_for_results: Optional[List[str]] = None,
    ) -> Response:
        if store_images_for_results is None:
            store_images_for_results = [
                EntryResult.NEW,
                EntryResult.REINIT,
                EntryResult.EXACT,
                EntryResult.HA,
                EntryResult.JUNK,
                EntryResult.NM,
                EntryResult.DET,
            ]

        data = dict(
            name=name,
            license_type=license_type,
            identify_facesize_threshold=identify_facesize_threshold,
            use_pps_time=use_pps_time,
            manual_create_facesize_threshold=manual_create_facesize_threshold,
            manual_create_on_ha=manual_create_on_ha,
            manual_create_on_junk=manual_create_on_junk,
            manual_identify_asm=manual_identify_asm,
            auto_create_persons=auto_create_persons,
            auto_create_facesize_threshold=auto_create_facesize_threshold,
            auto_create_check_blur=auto_create_check_blur,
            auto_create_check_exposure=auto_create_check_exposure,
            auto_create_on_ha=auto_create_on_ha,
            auto_create_on_junk=auto_create_on_junk,
            auto_check_face_angle=auto_check_face_angle,
            auto_check_liveness=auto_check_liveness,
            auto_create_liveness_only=auto_create_liveness_only,
            auto_identify_asm=auto_identify_asm,
            store_images_for_results=store_images_for_results,
        )
        try:
            return self.client.post(url="/v1/sources/", data=data)
        finally:
            self.client.close()

    def list(
        self, query: str = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"q": query, "limit": limit, "offset": offset}
        try:
            return self.client.get(url="/v1/sources/", params=data)
        finally:
            self.client.close()


class SourcesAsync(APIBaseAsync):
    async def create(
        self,
        name: str,
        license_type: str = SourceLicense.BASIC,
        identify_facesize_threshold: int = 7000,
        use_pps_time: bool = False,
        manual_create_facesize_threshold: int = 25000,
        manual_create_on_ha: bool = False,
        manual_create_on_junk: bool = False,
        manual_identify_asm: bool = True,
        auto_create_persons: bool = False,
        auto_create_facesize_threshold: int = 25000,
        auto_create_check_blur: bool = True,
        auto_create_check_exposure: bool = True,
        auto_create_on_ha: bool = False,
        auto_create_on_junk: bool = False,
        auto_check_face_angle: bool = True,
        auto_check_liveness: bool = False,
        auto_create_liveness_only: bool = True,
        auto_identify_asm: bool = True,
        store_images_for_results: Optional[List[str]] = None,
    ) -> Response:
        # TODO
        if store_images_for_results is None:
            store_images_for_results = [
                EntryResult.NEW,
                EntryResult.REINIT,
                EntryResult.EXACT,
                EntryResult.HA,
                EntryResult.JUNK,
                EntryResult.NM,
                EntryResult.DET,
            ]

        data = dict(
            name=name,
            license_type=license_type,
            identify_facesize_threshold=identify_facesize_threshold,
            use_pps_time=use_pps_time,
            manual_create_facesize_threshold=manual_create_facesize_threshold,
            manual_create_on_ha=manual_create_on_ha,
            manual_create_on_junk=manual_create_on_junk,
            manual_identify_asm=manual_identify_asm,
            auto_create_persons=auto_create_persons,
            auto_create_facesize_threshold=auto_create_facesize_threshold,
            auto_create_check_blur=auto_create_check_blur,
            auto_create_check_exposure=auto_create_check_exposure,
            auto_create_on_ha=auto_create_on_ha,
            auto_create_on_junk=auto_create_on_junk,
            auto_check_face_angle=auto_check_face_angle,
            auto_check_liveness=auto_check_liveness,
            auto_create_liveness_only=auto_create_liveness_only,
            auto_identify_asm=auto_identify_asm,
            store_images_for_results=store_images_for_results,
        )
        try:
            return await self.client.post(url="/v1/sources/", data=data)
        finally:
            await self.client.aclose()

    async def list(
        self, query: str = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"q": query, "limit": limit, "offset": offset}
        try:
            return await self.client.get(url="/v1/sources/", params=data)
        finally:
            await self.client.aclose()
