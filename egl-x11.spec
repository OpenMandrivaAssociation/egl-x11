%global major 1
%define libname %mklibname nvidia-egl-x11
%define lib32name %mklib32name nvidia-egl-x11

%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

Name:		egl-x11
Version:	1.0.4
Release:	1
Group:		System/Libraries
Summary:	X11 EGL External Platform library for nvidia GPUs
License:	MIT
URL:		https://github.com/NVIDIA/egl-x11
Source0:	https://github.com/NVIDIA/egl-x11/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	meson
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(eglexternalplatform) >= 1.0
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xdmcp)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(xcb-dri3)
BuildRequires:	pkgconfig(xcb-present)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(egl)

%if %{with compat32}
BuildRequires:	devel(libX11-xcb)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
BuildRequires:	devel(libX11-xcb)
BuildRequires:	devel(libdrm)
BuildRequires:	devel(libgbm)
BuildRequires:	devel(libxcb-dri3)
BuildRequires:	devel(libxcb-present)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libEGL)
%endif

Requires:	%{libname} >= %{EVRD}
# Required for directory ownership
Requires:	libglvnd-egl

%description
%{summary}.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
%{summary}.

%package -n %{lib32name}
Summary:	%{summary} (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
%{summary} (32-bit).

%files -n %{libname}
%doc README.md
%{_libdir}/*.so*
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xcb.json
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xlib.json

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/*.so*
%endif
